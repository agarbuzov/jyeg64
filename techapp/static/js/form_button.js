$(document).ready(function () {
    let x = 0;
    $('#add_btn').click(function () {
        $("#text_inputs").append('<p><label for="id_text">Text:</label><input type="text" name="text-'+x+'" required=""></p>')
        x++;
    })
    $('#remove_btn').click(function () {
        $('#text_inputs p:last').remove()
    })
})