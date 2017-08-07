function descargaCFDIs(){
  chrome.windows.getCurrent(
  	function (currentWindow) {
    	chrome.tabs.query(
    		{
    			active: true, 
    			windowId: currentWindow.id
    		},
    		function(activeTabs) {
    			chrome.tabs.executeScript(
    				activeTabs[0].id, {file: 'js/client.js', allFrames: true}
    			);
    		}
    	);
  	}
  );
}

window.onload = function() {
  document.getElementById('descarga').onclick = descargaCFDIs;
};