/////on attend que la page est chargée
window.addEventListener('load', (event) => {

  ///quand la personne veut remettre des images on supprime les existantes
  document.getElementById("id_image").addEventListener("click", function(){
    /////Delete image when we click on add image
        var element=document.querySelectorAll('.image');
        Array.prototype.forEach.call( element, function( node ) {
          node.parentNode.removeChild( node );
      });

  });

  ////Accept que les fichiers images(jpg,png....)
  var fileInput=document.getElementById('id_image');
  fileInput.accept="image/*"

  ////varriables globales
  var fileList=[];
  var image3;
  var image2;
  var image1;
  var title1;
  var title2;
  var title3;
  var tab=[];
  var name1;
  var name2;
  var bool=false;


  ///////POST
  var form = document.forms.namedItem("file-catcher");

  form.addEventListener('submit', (e) => {
    // on form submission, prevent default
    e.preventDefault();

    // construct a FormData object, which fires the formdata event
    new FormData(form);
  });

  form.addEventListener('formdata', (e) => {
    console.log('formdata fired');
    var numImg=document.querySelectorAll('.image');
    var changeOrder=document.querySelectorAll('.image');
    var it=[];
    for(var j=0;j<numImg.length;j++){
        image1 = document.getElementById("img"+j);
          it=it+' '+image1.title;
      }



    e.formData.set("name",it)
    // Get the form data from the event object
    let data = e.formData;


    for (var value of data.values()) {
        console.log(value)
    }
    let request = new XMLHttpRequest();
    request.open("POST","/createPost/");
    request.send(data);

    // submit the data via XHR
    var element=document.querySelectorAll('.image');
    Array.prototype.forEach.call( element, function( node ) {
      node.parentNode.removeChild( node );
  });
  document.getElementById('id_title').value="";
  document.getElementById('id_text').value="";
  });

  swap=document.getElementById('swap');

  //////////Image swap
  swap.addEventListener('click',(e)=>{
    function swapImages(){
        var numImg=document.querySelectorAll('.image');
        var changeOrder=document.querySelectorAll('.image');
        numImg=numImg.length;


        for(var j=0;j<numImg;j++){
          if(document.getElementById("img"+(j+1))){
            image1 = document.getElementById("img"+j);
            image2 = document.getElementById("img"+(j+1));

            title1=image1.title;
            title2=image2.title;


             image3=image1.src;
             title3=image1.title;

             image1.src = image2.src;
             image1.title=image2.title;

             image2.src = image3;
             image2.title=title3;
          }

        }

      }
      swapImages();
  });


  ////////Prévisualisation des images
  fileInput.addEventListener('change',function(e){

    fileList=[];

      for(var i=0;i<fileInput.files.length;i++){
        fileList.push(fileInput.files[i]);
      }
    previewFiles()
  });

  function previewFiles() {

    const files  = document.querySelector('input[type=file]').files;
    const preview  = document.getElementById('imagepreview');
    var i=0;
    var name="fill";
    var nameImage="img";

    document.getElementById('submit').style.display = "none";
    document.getElementById('swap').style.display = "none";
    if(files.length<20){
      setTimeout(function(){
          document.getElementById('submit').style.display = "block";
          document.getElementById('swap').style.display = "block";
         },

      1000);
    }else if((files.length>20)&& (files.length<40)){
        setTimeout(function(){
            document.getElementById('submit').style.display = "block";
            document.getElementById('swap').style.display = "block";
          },
        2000);
      }else if((files.length>50)&& (files.length<80)){
          setTimeout(function(){
              document.getElementById('submit').style.display = "block";
              document.getElementById('swap').style.display = "block";
            },
          3000);
        }else {
            setTimeout(function(){
                document.getElementById('submit').style.display = "block";
                document.getElementById('swap').style.display = "block";
              },
            6000);
          }

    function readAndPreview(file) {
      // Make sure `file.name` matches our extensions criteria
      if ( /\.(jpe?g|png|gif)$/i.test(file.name) ) {
        var reader = new FileReader();

        reader.addEventListener("load", function () {
            var div = document.createElement('div');
            div.setAttribute('class', name);
            div.id=name;
            div.style.float="left";
            div.style.padding="2px"
            preview.appendChild(div);
            name="fill"+i;
            nameImage="img"+i;
            nameButton="button"+i;


            var image = new Image();
            image.height = 100;
            image.id=nameImage;
            image.setAttribute('class', 'image');
            image.title = file.name;
            image.src = this.result;
            image.draggable=true;
            div.appendChild( image );
            i++;
        }, false);

        reader.readAsDataURL(file);

      }

    }

    if (files) {
      [].forEach.call(files, readAndPreview);

      for (prop in files){
        files[prop]=null
      }

    }

  }




  //////Enlève le bouton le temps du chargement des images
  document.getElementById("image-preview__image").style.display = "none";
});
