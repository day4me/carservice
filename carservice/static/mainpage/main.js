var coll = document.getElementsByClassName("collapsible");

var i;

for (let i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
	  for (let j = 0; j < coll.length; j++){
		  //console.log('j=' + j);
		   if ( coll[j].classList.contains('active') && j!=i){
			   //console.log('toggled on ' + j);
			   $(coll[j]).click();
		   }
		
	  }
    this.classList.toggle("active");
    var content = document.getElementById('content-' + (i));
    if (content.style.maxHeight){
	  content.style.maxHeight = null;
	  coll[i].style.color = '';
    } else {
		coll[i].style.color = '#e4324c';
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}