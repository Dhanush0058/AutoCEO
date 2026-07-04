import React, { useState } from 'react';
import { Plus, Mic, AudioLines, Code, Edit3, GraduationCap, Coffee, Lightbulb } from 'lucide-react';

interface HomeViewProps {
  onSendMessage: (msg: string) => void;
  isLoading: boolean;
}

export function HomeView({ onSendMessage, isLoading }: HomeViewProps) {
  const [input, setInput] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim() && !isLoading) {
      onSendMessage(input);
      setInput('');
    }
  };

  return (
    <div className="flex-1 flex flex-col items-center justify-center h-screen px-4 bg-[#212121]">
      <div className="w-full max-w-3xl flex flex-col items-center gap-8 -mt-20">
        <h1 className="serif-heading text-4xl md:text-5xl text-[#ececec] font-medium flex items-center gap-3">
          <span className="text-[#E07A5F]"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"></path></svg></span>
          Good morning, CEO
        </h1>

        <div className="w-full relative group">
          <form onSubmit={handleSubmit} className="w-full bg-[#2f2f2f] border border-[#404040] rounded-2xl flex flex-col min-h-[140px] p-3 transition-colors focus-within:border-[#555555] focus-within:bg-[#333333]">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault();
                  handleSubmit(e);
                }
              }}
              placeholder="How can I help you today?"
              className="w-full bg-transparent text-[#ececec] placeholder-[#737373] resize-none outline-none flex-1 p-2 text-[15px]"
              disabled={isLoading}
            />
            
            <div className="flex items-center justify-between pt-2 px-1">
              <button type="button" className="p-2 text-[#a3a3a3] hover:text-[#ececec] hover:bg-[#404040] rounded-lg transition-colors">
                <Plus className="w-5 h-5" />
              </button>
              
              <div className="flex items-center gap-2">
                <span className="text-xs text-[#a3a3a3] mr-2">AutoCEO 1.0 High </span>
                <button type="button" className="p-2 text-[#a3a3a3] hover:text-[#ececec] hover:bg-[#404040] rounded-lg transition-colors">
                  <Mic className="w-5 h-5" />
                </button>
                <button type="button" className="p-2 text-[#a3a3a3] hover:text-[#ececec] hover:bg-[#404040] rounded-lg transition-colors">
                  <AudioLines className="w-5 h-5" />
                </button>
              </div>
            </div>
          </form>
        </div>

        <div className="flex flex-wrap items-center justify-center gap-2 mt-4">
          <button 
            onClick={() => { setInput("What's our current runway?"); handleSubmit(new Event('submit') as any); }}
            className="flex items-center gap-2 px-4 py-2 bg-[#2f2f2f] hover:bg-[#404040] border border-[#404040] rounded-full text-sm text-[#ececec] transition-colors"
          >
            <Coffee className="w-4 h-4" /> Check Runway
          </button>
          <button 
            onClick={() => { setInput("Draft a JD for a Senior Backend Engineer"); handleSubmit(new Event('submit') as any); }}
            className="flex items-center gap-2 px-4 py-2 bg-[#2f2f2f] hover:bg-[#404040] border border-[#404040] rounded-full text-sm text-[#ececec] transition-colors"
          >
            <Edit3 className="w-4 h-4" /> Draft Job Description
          </button>
          <button 
            onClick={() => { setInput("Generate a standard NDA for a contractor"); handleSubmit(new Event('submit') as any); }}
            className="flex items-center gap-2 px-4 py-2 bg-[#2f2f2f] hover:bg-[#404040] border border-[#404040] rounded-full text-sm text-[#ececec] transition-colors"
          >
            <Code className="w-4 h-4" /> Generate Contract
          </button>
          <button 
            onClick={() => { setInput("Analyze top 3 competitors in our space"); handleSubmit(new Event('submit') as any); }}
            className="flex items-center gap-2 px-4 py-2 bg-[#2f2f2f] hover:bg-[#404040] border border-[#404040] rounded-full text-sm text-[#ececec] transition-colors"
          >
            <Lightbulb className="w-4 h-4" /> Market Analysis
          </button>
        </div>
      </div>
    </div>
  );
}
