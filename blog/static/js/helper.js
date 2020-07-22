
window.onload = function() {
	var CV_div = document.getElementById('CV_full');
	var blog_div = document.getElementById("blog_div");
	var summary_div = document.getElementById("summary-div1")

	document.getElementById("CV_viewfull").onclick = function() {
	  if(this.innerHTML === 'View full CV') 
	  { 

	    this.innerHTML = 'Close';
	    CV_div.className = 'fade-in';
	    blog_div.className = "slide-out";
	    summary_div.id = "summary-div2"


	  } else {
	    this.innerHTML = 'View full CV';
	    
	    CV_div.className = 'fade-out'; 
	    blog_div.className = "slide-in";
	    summary_div.id = "summary-div1"


	  }  
	}
}




  



