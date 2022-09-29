Dropzone.autoDiscover=false;
$(document).ready(function () {
    const myDropzone = new Dropzone('#my-dropzone', {
        autoProcessQueue: false,
        url: 'upload/',
        maxFiles: 1,
        maxFilesize: 2,
        acceptedFiles: '.pdf',
        clickable:true,
        disablePreviews:false,

    })



    $("#uploadButton").click(function (e) {
    console.log("clicked");
    // e.preventDefault();

    myDropzone.processQueue();
});
})
