import React from 'react';
import { DollarSign, TrendingDown } from 'lucide-react';

export function FinancialWidget() {
  return (
    <div className="glass-panel rounded-xl p-4">
      <div className="flex items-center justify-between mb-4">
        <h2 className="font-semibold text-gray-200 flex items-center gap-2">
          <DollarSign className="w-5 h-5 text-emerald-400" />
          Financial Pulse
        </h2>
        <span className="text-xs px-2 py-1 bg-emerald-900/30 text-emerald-400 rounded-full border border-emerald-800/50">
          Live
        </span>
      </div>
      
      <div className="grid grid-cols-2 gap-4">
        <div className="bg-gray-900/50 p-3 rounded-lg border border-gray-800">
          <div className="text-sm text-gray-400 mb-1">Runway</div>
          <div className="text-2xl font-bold text-gray-100">8.8 <span className="text-sm font-normal text-gray-500">months</span></div>
        </div>
        <div className="bg-gray-900/50 p-3 rounded-lg border border-gray-800">
          <div className="text-sm text-gray-400 mb-1">Burn Rate</div>
          <div className="text-xl font-bold text-gray-100 flex items-center gap-2">
            $45K <TrendingDown className="w-4 h-4 text-red-400" />
          </div>
        </div>
      </div>
    </div>
  );
}
