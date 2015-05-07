function resolvePose(links,angles)
{
	links[2].rotation.x = angles[1];
}

function drawRobot()
{
	var scene = new THREE.Scene();
	var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
	camera.position.y = 500;
 
	var renderer = new THREE.WebGLRenderer();
	renderer.setSize(window.innerWidth, window.innerHeight);
	document.body.appendChild(renderer.domElement);

	//////////////////
	/* リンクの情報 */
	//////////////////
	var links = new Array(6);
	var h = new Array(6);

	/* LINK 1 */
	//上の半径、下の半径、高さ、上下の分割、横の分割、蓋を閉じるか
	r = 155.0/2;
	h[0] = 180.0;
	geometry = new THREE.CylinderGeometry(r,r,h[0],20,0,false);
	material = new THREE.MeshBasicMaterial({color: 0x999999});
	links[0] = new THREE.Mesh(geometry, material);
	links[0].position.x = 0.0;
	links[0].position.y = h[0]/2;
	links[0].position.z = -1000.0;
	scene.add(links[0]);

	/* LINK 2 */
	r = 116.0/2;
	h[1] = 120.0;
	geometry = new THREE.CylinderGeometry(r,r,h[1],20,0,false);
	material = new THREE.MeshBasicMaterial({color: 0xaaaaaa});
	links[1] = new THREE.Mesh(geometry, material);
	links[1].position.x = 0.0;
	links[1].position.y = h[0] + h[1]/2;
	links[1].position.z = -1000.0;
	scene.add(links[1]);

	/* LINK 3 */
	r = 160.0/2;
	h[2] = 250.0;
	geometry = new THREE.CylinderGeometry(r,r,h[2],20,0,false);
	material = new THREE.MeshBasicMaterial({color: 0xbbbbbb});
	links[2] = new THREE.Mesh(geometry, material);
	links[2].position.x = 0.0;
	links[2].position.y = h[0] + h[1] + h[2]/2;
	links[2].position.z = -1000.0;
	scene.add(links[2]);

	/* LINK 4 */
	r = 116.0/2;
	h[3] = 160.0;
	geometry = new THREE.CylinderGeometry(r,r,h[3],20,0,false);
	material = new THREE.MeshBasicMaterial({color: 0xcccccc});
	links[3] = new THREE.Mesh(geometry, material);
	links[3].position.x = 0.0;
	links[3].position.y = h[0] + h[1] + h[2] + h[3]/2;
	links[3].position.z = -1000.0;
	scene.add(links[3]);

	/* LINK 5 */
	r = 80.0/2;
	h[4] = 72.0;
	geometry = new THREE.CylinderGeometry(r,r,h[4],20,0,false);
	material = new THREE.MeshBasicMaterial({color: 0xdddddd});
	links[4] = new THREE.Mesh(geometry, material);
	links[4].position.x = 0.0;
	links[4].position.y = h[0] + h[1] + h[2] + h[3] + h[4]/2;
	links[4].position.z = -1000.0;
	scene.add(links[4]);

	var render = function () {
		requestAnimationFrame(render);
		angles = [0.0,45.0,0.0,0.0,0.0];
		resolvePose(links,angles);
		renderer.render(scene, camera);
	};
	render();
}
