import React from 'react';
import { ListTodo, ShieldAlert } from 'lucide-react';

export function TaskTracker() {
  return (
    <div className="glass-panel rounded-xl flex flex-col h-full">
      <div className="p-4 border-b border-gray-800 bg-gray-900/50 flex items-center justify-between">
        <h2 className="font-semibold text-gray-200 flex items-center gap-2">
          <ListTodo className="w-5 h-5 text-purple-400" />
          Approvals & Tasks
        </h2>
        <span className="flex h-5 w-5 items-center justify-center rounded-full bg-red-500/20 text-xs font-medium text-red-500 border border-red-500/30">
          1
        </span>
      </div>
      
      <div className="p-4 flex-1 overflow-y-auto space-y-3">
        {/* Mock Approval Task */}
        <div className="bg-red-900/10 border border-red-900/30 p-3 rounded-lg">
          <div className="flex items-start gap-3">
            <ShieldAlert className="w-5 h-5 text-red-400 mt-0.5 shrink-0" />
            <div>
              <h3 className="text-sm font-medium text-red-200">Approve CTO Offer Letter</h3>
              <p className="text-xs text-gray-400 mt-1">Legal agent generated the offer letter for John Doe with $150K salary and 1% equity.</p>
              <div className="flex gap-2 mt-3">
                <button className="text-xs px-3 py-1.5 bg-red-600 hover:bg-red-500 text-white rounded-md transition-colors">
                  Review & Approve
                </button>
                <button className="text-xs px-3 py-1.5 bg-gray-800 hover:bg-gray-700 text-gray-300 rounded-md transition-colors border border-gray-700">
                  Reject
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
