import { useState } from 'react';
import { Sidebar } from '../components/layout/Sidebar';
import { HomeView } from '../components/dashboard/HomeView';
// Import AgentFeed and FinancialWidget if we want to show them after a query,
// but the screenshot is just the home state. Let's build the home state first.

export function Dashboard() {
  const [isLoading, setIsLoading] = useState(false);
  const [activities, setActivities] = useState<any[]>([]);
  const [hasQueried, setHasQueried] = useState(false);
  const [currentQuery, setCurrentQuery] = useState("");
  const [activeInput, setActiveInput] = useState("");

  const handleSendMessage = async (msg: string) => {
    setIsLoading(true);
    setHasQueried(true);
    setCurrentQuery(msg);
    setActiveInput("");
    
    // Clear previous activities for the new query
    setActivities([]);
    
    const newActivity = {
      id: Date.now().toString(),
      agent: 'Orchestrator',
      action: `Processing query: "${msg}"`,
      status: 'running' as const,
      time: new Date().toLocaleTimeString(),
    };
    setActivities([newActivity]);

    try {
      const response = await fetch('http://localhost:8000/api/orchestrator/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: msg })
      });
      const data = await response.json();
      
      setActivities(prev => prev.map(a => a.id === newActivity.id ? { ...a, status: 'success' } : a));
      
      data.agent_responses.forEach((resp: any, idx: number) => {
        setTimeout(() => {
          setActivities(prev => [...prev, {
            id: Date.now().toString() + idx,
            agent: resp.agent_name,
            action: resp.message,
            status: 'success' as const,
            time: new Date().toLocaleTimeString(),
          }]);
        }, (idx + 1) * 800);
      });
      
    } catch (error) {
      console.error(error);
      setActivities(prev => prev.map(a => a.id === newActivity.id ? { ...a, status: 'pending' } : a));
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex h-screen bg-[#212121] text-[#ececec]">
      <Sidebar />
      
      {/* Main Content Area */}
      {!hasQueried ? (
        <HomeView onSendMessage={handleSendMessage} isLoading={isLoading} />
      ) : (
        <div className="flex-1 flex flex-col">
          <div className="flex-1 p-6 overflow-y-auto">
            {/* Active chat view */}
            <div className="max-w-3xl mx-auto space-y-6 mt-8">
               <div className="flex justify-end">
                 <div className="inline-block bg-[#2f2f2f] text-[#ececec] p-4 rounded-2xl rounded-tr-sm max-w-[80%]">
                   {currentQuery}
                 </div>
               </div>
               <div className="text-left flex gap-4">
                  <div className="w-8 h-8 rounded-full bg-[#E07A5F] flex items-center justify-center shrink-0">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"></path></svg>
                  </div>
                 <div className="flex-1 space-y-4">
                   <p className="font-medium text-lg">AutoCEO Orchestrator</p>
                   <div className="space-y-2">
                     {activities.map(a => (
                       <div key={a.id} className="text-[15px] bg-[#2a2a2a] p-3 rounded-lg border border-[#333] flex items-start gap-3">
                         <div className="mt-0.5">
                           {a.status === 'success' ? <span className="text-emerald-400">✓</span> : <span className="text-blue-400 animate-spin inline-block">⟳</span>}
                         </div>
                         <div>
                           <div className="text-xs text-[#a3a3a3] mb-1 font-semibold">{a.agent}</div>
                           <div className="text-[#ececec]">{a.action}</div>
                         </div>
                       </div>
                     ))}
                   </div>
                   {isLoading && (
                     <div className="flex gap-1 items-center h-8">
                       <span className="w-2 h-2 bg-[#a3a3a3] rounded-full animate-bounce"></span>
                       <span className="w-2 h-2 bg-[#a3a3a3] rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></span>
                       <span className="w-2 h-2 bg-[#a3a3a3] rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></span>
                     </div>
                   )}
                 </div>
               </div>
            </div>
          </div>
          {/* Chat input at bottom for active chat */}
          <div className="p-4 max-w-3xl mx-auto w-full pb-8">
            <form 
              onSubmit={(e) => {
                e.preventDefault();
                if (activeInput.trim() && !isLoading) {
                  handleSendMessage(activeInput);
                }
              }}
              className="bg-[#2f2f2f] border border-[#404040] rounded-2xl flex items-center p-2 focus-within:border-[#555] transition-colors"
            >
              <input 
                type="text" 
                value={activeInput}
                onChange={(e) => setActiveInput(e.target.value)}
                disabled={isLoading}
                className="flex-1 bg-transparent border-none outline-none px-3 py-2 text-[#ececec] placeholder-[#737373]" 
                placeholder="Reply to AutoCEO..." 
              />
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
