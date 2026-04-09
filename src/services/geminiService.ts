import { GoogleGenAI, Type } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// Sequential queue for image generation to avoid 429s
let thumbnailQueue: Promise<any> = Promise.resolve();

export const geminiService = {
  async generateProjectImpact(title: string, description: string) {
    try {
      const response = await ai.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: `Generate 2-3 concise, high-impact bullet points summarizing the main achievements or functionalities of this project based on its title and description. 
        Project Title: ${title}
        Description: ${description}
        Return the result as a JSON array of strings.`,
        config: {
          responseMimeType: "application/json",
          responseSchema: {
            type: Type.ARRAY,
            items: { type: Type.STRING }
          }
        }
      });
      
      return JSON.parse(response.text);
    } catch (error) {
      console.error("Error generating project impact:", error);
      return ["Optimized system performance", "Enhanced user experience", "Scalable architecture"];
    }
  },

  async generateProjectThumbnail(id: number | string, title: string, techStack: string[]) {
    // Chain to the queue to ensure sequential execution
    const result = thumbnailQueue.then(async () => {
      // Add a small buffer between requests
      await new Promise(resolve => setTimeout(resolve, 1000));

      try {
        const prompt = `A professional, high-tech, minimalist 3D isometric illustration representing a software project titled "${title}". 
        It uses technologies like ${techStack.join(", ")}. 
        The style should be clean, modern, with a dark theme and indigo accents. 
        No text in the image. High quality, digital art.`;

        const response = await ai.models.generateContent({
          model: "gemini-2.5-flash-image",
          contents: {
            parts: [{ text: prompt }]
          },
          config: {
            imageConfig: {
              aspectRatio: "16:9",
              imageSize: "1K"
            }
          }
        });

        for (const part of response.candidates[0].content.parts) {
          if (part.inlineData) {
            return `data:image/png;base64,${part.inlineData.data}`;
          }
        }
        return `https://picsum.photos/seed/${id}-${encodeURIComponent(title)}/800/450`;
      } catch (error: any) {
        if (error?.status === 429 || error?.message?.includes('429') || error?.message?.includes('RESOURCE_EXHAUSTED')) {
          console.warn(`Thumbnail generation rate limited for "${title}". Using fallback.`);
        } else {
          console.error("Error generating project thumbnail:", error);
        }
        return `https://picsum.photos/seed/${id}-${encodeURIComponent(title)}/800/450`;
      }
    });

    // Update the queue pointer
    thumbnailQueue = result.catch(() => {}); 
    
    return result;
  }
};
