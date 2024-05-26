$(document).ready(function(){
    $('.like-button').click(function(e) {
        e.preventDefault();
        var postId = $(this).data('post-id');
        var icon = $('#like-icon-' + postId);

        $.ajax({
            type: "POST",
            url: `/forum/like/${postId}/`,
            data: {
                'csrfmiddlewaretoken': csrfToken
            },
            success: function(response) {
                $('#like-count-' + postId).html(response.likes)
                if (response.liked) {
                    icon.removeClass('far').addClass('fas');
                } else {
                    icon.removeClass('fas').addClass('far');
                }
            },
            error: function() {
                alert("Action failed.");
            }
        });
    });
});
$(document).ready(function(){
$('.like-comment-btn').click(function(e) {
    e.preventDefault();
    var commentId = $(this).data('comment-id');
    var icon = $('#like-icon-' + commentId);

    $.ajax({
        type: "POST",
        url: `/forum/like-comment/${commentId}/`,
        data: {
            'csrfmiddlewaretoken': csrfToken
        },
        success: function(response) {
            $('#like-count-' + commentId).html(response.likes_count + " Likes")
            if (response.liked) {
                icon.removeClass('far').addClass('fas');
            } else {
                icon.removeClass('fas').addClass('far');
            }
        },
        error: function() {
            alert("Action failed.");
        }
    });
});
});$(document).ready(function(){
$('.follow-button').click(function() {
    var button = $(this);
    var postId = button.data('post-id');
    $.ajax({
        url: `/forum/toggle-follow/${postId}/`,  // 确保这里的 URL 是正确的，适应您的应用路径
        type: 'POST',
        data: {
            csrfmiddlewaretoken: csrfToken,
        },
        success: function(response) {
            if(response.followed) {
                button.html('<i class="fas fa-heart"> 取消關注</i>');
            } else {
                button.html('<i class="far fa-heart"> 關注</i>');
            }
        },
        error: function(xhr, errmsg, err) {
            alert('操作失败: ' + errmsg);
        }
    });
});
});