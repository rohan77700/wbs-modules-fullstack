$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});

$(document).on("click", ".js-toggle-modal", function(e) {
    e.preventDefault()
    $(".js-modal").toggleClass("hidden")
})
.on("click", ".js-submit", function(e) {
    e.preventDefault()
    const title = $(".js-post-title").val().trim()
    const text = $(".js-post-text").val().trim()
    const $btn = $(this)

    if(!title.length || !text.length) {
        return false
    }

    $(".js-modal").addClass("hidden")
    $(".js-post-title").val('')
    $(".js-post-text").val('')

    $btn.prop("disabled", true).text("Posting!")
    $.ajax({
        type: 'POST',
        url: $(".js-post-title").data("post-url"),
        data: {
            title: title,
            text: text
        },
        success: (dataHtml) => {
            $(".js-modal").addClass("hidden");
            $("#posts-container").prepend(dataHtml);
            $btn.prop("disabled", false).text("New Post");
            $(".js-post-title").val('')
            $(".js-post-text").val('')
        },
        error: (error) => {
            console.warn(error)
            $btn.prop("disabled", false).text("Error");
        }
    });
})
.on("click", ".js-follow", function(e) {
    e.preventDefault()
    const action = $(this).attr("data-action")

    $.ajax({
        type: 'POST',
        url: $(this).data("url"),
        data: {
            action: action,
            username: $(this).data("username"),
        },
        success: (data) => {
            $(".js-follow-text").text(data.wording)
            if(action == "follow") {
                $(this).attr("data-action", "unfollow")
            } else {
                $(this).attr("data-action", "follow")
            }
        },
        error: (error) => {
            console.warn(error)
        }
    });
})
.on("click", ".js-toggle-dropdown > button", function(e) {
    e.preventDefault()
    $(".js-dropdown").toggleClass("hidden")
})
.on("click", ".js-dropdown > button", function(e) {
    e.preventDefault()
    const url = $(this).data("url")

    if(url) {
        window.location.href = url
    }
})