var ckClassicEditor=document.querySelectorAll(".ckeditor-classic");ckClassicEditor&&Array.from(ckClassicEditor).forEach(function(){ClassicEditor.create(document.querySelector(".ckeditor-classic")).then(function(e){e.ui.view.editable.element.style.height="200px"}).catch(function(e){console.error(e)})});const editor=SUNEDITOR.create(document.getElementById("sun_editor")||"sun_editor",{minHeight:"300px"});