function setImageUrl(imageUrl) {
    document.getElementById('image').src = imageUrl;

    const jcrop = Jcrop.attach('image');
    jcrop.listen('dblclick', function() {
        console.log("Ready to send")
    })
}
