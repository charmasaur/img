chrome.browserAction.onClicked.addListener(function() {
    // Take a screenshot of the current tab.
    chrome.tabs.captureVisibleTab(function(imageUrl) {
        // When the screenshot is taken, create a new tab to show the result.
        var snipImageUrl = chrome.runtime.getURL('snip_image.html')
        var snipImageTabId = null;

        chrome.tabs.onUpdated.addListener(function onUpdatedListener(tabId, changeInfo) {
            if (tabId != snipImageTabId) {
                // Wrong tab.
                return;
            }
            if (changeInfo.status == 'loading') {
                // Still loading.
                return;
            }
            chrome.tabs.onUpdated.removeListener(onUpdatedListener);

            var views = chrome.extension.getViews({tabId: snipImageTabId})
            if (views.length == 0) {
                alert("Failed to create tab.")
                return;
            }
            views[0].setImageUrl(imageUrl);
        });

        chrome.tabs.create({url: snipImageUrl}, function(tab) {
            snipImageTabId = tab.id;
        });
    });
});
