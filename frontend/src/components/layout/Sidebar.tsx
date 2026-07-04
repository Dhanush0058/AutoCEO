import React from 'react';
import { Plus, MessageSquare, FolderKanban, Component, Settings, Code, Users, PenTool, Download } from 'lucide-react';

export function Sidebar() {
  return (
    <div className="w-[260px] h-screen bg-[#171717] border-r border-[#333333] flex flex-col text-sm text-[#a3a3a3]">
      <div className="p-4 flex items-center justify-between">
        <h1 className="serif-heading text-[#ececec] text-xl font-medium tracking-wide">AutoCEO</h1>
        <div className="flex gap-2">
          <button className="hover:text-white"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></button>
          <button className="hover:text-white"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg></button>
        </div>
      </div>

      <div className="px-3 py-2">
        <button className="flex items-center gap-3 w-full p-2 hover:bg-[#2f2f2f] rounded-md transition-colors text-[#ececec]">
          <Plus className="w-4 h-4" />
          <span>New chat</span>
        </button>
      </div>

      <div className="px-3 py-2 space-y-1 flex-1 overflow-y-auto">
        <div className="pt-4 pb-1 px-2 text-xs font-semibold text-[#666666]">Overview</div>
        <button className="flex items-center gap-3 w-full p-2 hover:bg-[#2f2f2f] rounded-md transition-colors">
          <MessageSquare className="w-4 h-4" />
          <span>Dashboard</span>
        </button>
        <button className="flex items-center gap-3 w-full p-2 hover:bg-[#2f2f2f] rounded-md transition-colors">
          <FolderKanban className="w-4 h-4" />
          <span>Pending Approvals</span>
        </button>
        
        <div className="pt-4 pb-1 px-2 text-xs font-semibold text-[#666666]">Specialist Agents</div>
        <button className="flex items-center gap-3 w-full p-2 hover:bg-[#2f2f2f] rounded-md transition-colors">
          <Code className="w-4 h-4" />
          <span>Finance</span>
        </button>
        <button className="flex items-center gap-3 w-full p-2 hover:bg-[#2f2f2f] rounded-md transition-colors">
          <Users className="w-4 h-4" />
          <span>HR & Hiring</span>
        </button>
        <button className="flex items-center gap-3 w-full p-2 hover:bg-[#2f2f2f] rounded-md transition-colors">
          <Component className="w-4 h-4" />
          <span>Legal & Compliance</span>
        </button>
        <button className="flex items-center gap-3 w-full p-2 hover:bg-[#2f2f2f] rounded-md transition-colors">
          <PenTool className="w-4 h-4" />
          <span>Go-to-Market</span>
        </button>

        <div className="pt-4 pb-1 px-2 text-xs font-semibold text-[#666666]">Settings</div>
        <button className="flex items-center gap-3 w-full p-2 hover:bg-[#2f2f2f] rounded-md transition-colors">
          <Settings className="w-4 h-4" />
          <span>Integrations</span>
        </button>
      </div>

      <div className="p-3 border-t border-[#333333]">
        <button className="flex items-center justify-between w-full p-2 hover:bg-[#2f2f2f] rounded-md transition-colors">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 bg-blue-900 text-blue-200 rounded-full flex items-center justify-center font-medium text-xs">
              FD
            </div>
            <div className="text-left flex flex-col">
              <span className="text-sm font-medium text-[#ececec]">Founder</span>
              <span className="text-xs text-[#a3a3a3]">Admin</span>
            </div>
          </div>
          <Settings className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
