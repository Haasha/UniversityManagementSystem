	var Count=0;
	function myFunction(x) {
		x.classList.toggle("change");

		if(Count%2==0){
			openNav();
			Count=1;
		}else{
			closeNav();
			Count=0;
		}
	}
	function openNav() {
	  document.getElementById("mySidenav").style.width = "150px";
	}

	function closeNav() {
	  document.getElementById("mySidenav").style.width = "0";
	}