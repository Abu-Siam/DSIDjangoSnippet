var Drop = Dropzone.options.DidDropzone = {
            url: 'upload/',

    autoProcessQueue: true, //stops from uploading files until user submits form
    paramName: "pdf", // The name that will be used to transfer the file
    maxFilesize: 0.5, // Maximum size of file that you will allow (MB)
    clickable: true, // This allows the dropzone to select images onclick
    acceptedFiles: '.pdf', //accepted file types
    maxFiles: 1, //Maximum number of files/images in dropzone
    parallelUploads: 10,
    maxfilesexceeded : function (files) {
            this.removeAllFiles();
            this.addFile(files);
     },


    init: function(){

        var submitButton = document.querySelector("#image-btn")
        var url = $('#DidDropzone').attr("action")
        myDropzone = this;

        //process the queued images on click
        submitButton.addEventListener("click", function() {
            myDropzone.processQueue();
        });

        //fire the images to url
        myDropzone.on("processing", function(file) {
          myDropzone.options.url = url;
        });

        //clear the dropzone when complete
        myDropzone.on("complete", function(file) {
            myDropzone.removeFile(file);
        });
    },
    success: function(file, json){

        // alert("Perfect! Now visit your gallery...")

    },
}

// Dropzone.autoDiscover=false;
// $(document).ready(function () {
//     const myDropzone = new Dropzone('#DidDropzone', {
//         autoProcessQueue: true,
//         url: 'upload/',
//         maxFiles: 1,
//         maxFilesize: 2,
//         acceptedFiles: '.pdf',
//         clickable:true,
//         disablePreviews:false,
//
//     })
//
//
//
//     $("#uploadButton").click(function (e) {
//     console.log("clicked");
//     // e.preventDefault();
//
//     myDropzone.processQueue();
// });
// })
