export type AnalyticsEvent = 
  | { type: 'click_hire_me'; location: 'nav' | 'hero' }
  | { type: 'click_project_link'; projectTitle: string; linkType: 'github' | 'live' | 'case_study' }
  | { type: 'chat_message_sent'; messageLength: number }
  | { type: 'chat_opened' }
  | { type: 'form_submission_success'; formName: string }
  | { type: 'form_submission_error'; formName: string; error: string }
  | { type: 'form_field_focus'; formName: string; fieldName: string }
  | { type: 'form_field_blur'; formName: string; fieldName: string; duration?: number }
  | { type: 'form_field_input'; formName: string; fieldName: string; valueLength: number };

class AnalyticsService {
  private isEnabled: boolean = true;

  track(event: AnalyticsEvent) {
    if (!this.isEnabled) return;

    // In a real app, you would send this to Google Analytics, Mixpanel, etc.
    console.log(`[Analytics] ${event.type}`, event);

    // Example: window.gtag?.('event', event.type, event);
  }

  setEnabled(enabled: boolean) {
    this.isEnabled = enabled;
  }
}

export const analytics = new AnalyticsService();
