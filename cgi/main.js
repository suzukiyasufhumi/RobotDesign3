function sendAngles(){
	var httpReq = new XMLHttpRequest();
	httpReq.onreadystatechange = function(){
		if(httpReq.readyState != 4 || httpReq.status != 200)
			return;

		document.getElementById("debug").innerHTML = httpReq.responseText;
	}
	//var url = "/ajax/last_articles.cgi?num=" + num;
	var url = "/sendAngles.ajax.py?angles="
	for (i=1;i<=6;i++){
		if(i==4)continue;
		angle = document.getElementById("J" + i).value;
		url += angle + ',';
	}
	url = url.replace(/,$/,"");
	httpReq.open("GET",url,true);
	httpReq.send(null);
}
