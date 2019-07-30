function setImageUrl(imageUrl) {
    const image = document.getElementById('image')

    image.setAttribute("crossOrigin", "anonymous");
    image.src = imageUrl;

    const jcrop = Jcrop.attach('image');

    jcrop.listen('dblclick', function() {
        const canvas = document.getElementById('canvas')

        // Prepare temporary canvas with the appropriate dimensions.
        const r = Jcrop.Rect.from(jcrop.active.el)
        canvas.width = r.w
        canvas.height = r.h

        // Render cropped area into temporary canvas, and grab data URL.
        const context = canvas.getContext('2d');
        context.drawImage(image, r.x, r.y, r.w, r.h, 0, 0, r.w, r.h);
        const croppedImageUrl = canvas.toDataURL();

        // Convert data URL to blob, and when that's ready post it to romper-image.
        fetch(croppedImageUrl)
            .then(croppedImage => croppedImage.blob())
            .then(function(croppedImageBlob) {
                // Prepare form data.
                const formData = new FormData;
                formData.append("image", croppedImageBlob);

                // Send data. If all is successful, redirect to the uploaded image.
                fetch("https://romper-image.appspot.com/upload", {
                    method: 'POST',
                    body: formData
                })
                .then(function(response) {
                    if (response.status != 200) {
                      return Promise.reject(new Error(response.statusText));
                    }
                    return Promise.resolve(response);
                })
                .then(response => response.text())
                .then(responseText => window.location.replace(responseText))
                .catch(error => console.log("Error uploading", error));
            });
    });
}
