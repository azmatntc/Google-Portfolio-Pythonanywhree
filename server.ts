import express from "express";
import { createServer as createViteServer } from "vite";
import path from "path";
import { fileURLToPath } from "url";
import { GoogleGenAI } from "@google/genai";
import dotenv from "dotenv";

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function startServer() {
  const app = express();
  const PORT = 3000;

  app.use(express.json());

  // API routes
  app.get("/api/health", (req, res) => {
    res.json({ status: "ok", message: "Django Mock API is running" });
  });

  app.post("/api/leads", (req, res) => {
    const { name, email, message } = req.body;
    if (!name || !email || !message) {
      return res.status(400).json({ message: "All fields are required" });
    }
    console.log("Lead captured:", req.body);
    res.status(201).json({ status: "success", message: "Lead captured successfully" });
  });

  app.get("/api/projects", (req, res) => {
    res.json([
      {
        id: 1,
        title: "AI Portfolio Architect",
        description: "A full-stack portfolio generator with Django and Svelte.",
        tech_stack: ["Django", "Svelte", "MySQL", "Gemini"],
        github_link: "https://github.com/example/portfolio",
        live_demo: "#",
        tags: ["Full-Stack", "AI", "Automation"]
      },
      {
        id: 2,
        title: "Cloud Automation Tool",
        description: "Infrastructure as code automation for AWS.",
        tech_stack: ["Python", "Terraform", "AWS"],
        github_link: "https://github.com/example/cloud-auto",
        live_demo: "#",
        tags: ["DevOps", "Cloud"]
      }
    ]);
  });

  // Django Admin Info Route
  app.get("/admin", (req, res) => {
    res.send(`
      <div style="font-family: sans-serif; padding: 40px; max-width: 600px; margin: auto; line-height: 1.6;">
        <h1 style="color: #4f46e5;">Django Admin Panel</h1>
        <p>The Django Admin Panel is fully configured in the codebase but runs on the <strong>Python backend</strong>.</p>
        <div style="background: #f3f4f6; padding: 20px; border-radius: 12px; border: 1px solid #e5e7eb;">
          <h3 style="margin-top: 0;">How to access:</h3>
          <ol>
            <li>Deploy to <strong>PythonAnywhere</strong>.</li>
            <li>Run <code>python manage.py createsuperuser</code> in the console.</li>
            <li>Visit <code>/admin</code> on your live domain.</li>
          </ol>
        </div>
        <p style="margin-top: 20px; color: #6b7280; font-size: 0.9em;">
          Note: In this preview environment, we use a Node.js mock server for speed. 
          The real Django Admin requires a Python environment to execute.
        </p>
        <a href="/" style="display: inline-block; margin-top: 20px; color: #4f46e5; font-weight: bold; text-decoration: none;">&larr; Back to Portfolio</a>
      </div>
    `);
  });

  // AI Chat Proxy
  app.post("/api/chat", async (req, res) => {
    try {
      const { message } = req.body;
      const apiKey = process.env.GEMINI_API_KEY;
      if (!apiKey) {
        return res.status(500).json({ error: "Gemini API key not configured" });
      }

      const genAI = new GoogleGenAI({ apiKey });
      const response = await genAI.models.generateContent({
        model: "gemini-3-flash-preview",
        contents: message,
      });
      res.json({ reply: response.text });
    } catch (error) {
      console.error("AI Chat Error:", error);
      res.status(500).json({ error: "Failed to process AI request" });
    }
  });

  if (process.env.NODE_ENV !== "production") {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(__dirname, "dist");
    app.use(express.static(distPath));
    app.get("*", (req, res) => {
      res.sendFile(path.join(distPath, "index.html"));
    });
  }

  app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on http://localhost:${PORT}`);
  });
}

startServer();
