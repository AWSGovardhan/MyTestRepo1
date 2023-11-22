$(document).ready(function () {
    // URL of the RSS feed
    var rssFeedUrl = 'https://example.com/rss-feed.xml';

    // Fetch the RSS feed using jQuery's AJAX
    $.ajax({
        url: 'https://api.rss2json.com/v1/api.json',
        method: 'GET',
        dataType: 'json',
        data: {
            rss_url: rssFeedUrl
        },
        success: function (data) {
            // Check if the request was successful
            if (data.status === 'ok') {
                // Process the feed items and display them
                displayFeedItems(data.items);
            } else {
                console.error('Error fetching RSS feed:', data.message);
            }
        },
        error: function (error) {
            console.error('Error fetching RSS feed:', error);
        }
    });

    // Function to display feed items in the HTML
    function displayFeedItems(items) {
        var feedContainer = $('#rss-feed');

        // Iterate through each feed item and append it to the container
        items.forEach(function (item) {
            var feedItem = '<div class="feed-item">' +
                                '<h2><a href="' + item.link + '" target="_blank">' + item.title + '</a></h2>' +
                                '<p>' + item.description + '</p>' +
                            '</div>';

            feedContainer.append(feedItem);
        });
    }
});
