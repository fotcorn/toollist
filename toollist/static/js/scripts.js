$(document).ready(function () {
    // open up comment row
    $('.trigger_comment').on('click', function () {
        var next = $(this).next();

        if (next.hasClass('comment_show')) {
            next.removeClass('comment_show');
        } else {
            $('.comment_show').removeClass('comment_show');
            next.addClass('comment_show');
        }
    });

    // stick list header
    $('.toollist-table').stickyTableHeaders({fixedOffset: $('.navbar') });


    // status change drop down
    var statusSelect = $('.status-select')

    statusSelect.change(function () {
        var form = $(this).parent('form');
        form.find('.scroll').val(window.scrollY);
        form.submit();
    })

    statusSelect.click(function () {
        return false;
    });

    // scroll to old position on status change
    var queryDict = {}
    location.search
        .substr(1)
        .split("&")
        .forEach(function(item) {
            queryDict[item.split("=")[0]] = item.split("=")[1]
        })
    var scroll = parseInt(queryDict['scroll']);
    if (!isNaN(scroll)) {
        window.scroll(0, scroll);
    }
});
