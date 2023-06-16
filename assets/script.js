function add_or_remove_favourite(item, csrf_token) {
    console.log(csrf_token)
    let product_id = item.data('product_id'),
        star = item.find('.bi');
    $.get(
        `/favourites/ajax/${product_id}`
    ).done(function (data) {
        if (data.is_favourite === true) {
            star.addClass('bi bi-star-fill').removeClass('bi bi-star')
        } else {
            star.addClass('bi bi-star').removeClass('bi bi-star-fill')
        }
    }).fail(function (error) {
        console.log(error)
    })
}