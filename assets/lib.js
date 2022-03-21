// Earthquake marker
function getColor(d) {
	return d <= 50 ? '#FF0000' :
		d <= 100 ? '#FFA500' :
			d <= 250 ? '#FFFF00' :
				d <= 600 ? '#008000' :
					'#0000FF';
}
			
window.myEq = Object.assign({}, window.myEq, {  
    myMarkerEq: { 
        pointToLayer: function(feature, latlng, context) {  
			return L.circleMarker(latlng, {
				radius: feature.properties.mag * 2,
				fillColor: getColor(feature.properties.depth),
				color: '#000000',
				weight: 1,
				opacity: 1,
				fillOpacity: 0.8
			}); 
        },
		bindPopup: function(feature, layer) {
			var reader = new XMLHttpRequest();
			var checkFor = "https://bmkg-content-inatews.storage.googleapis.com/mt." + feature.properties.id + ".png";
			reader.open('get', checkFor, true);
			reader.onreadystatechange = checkReadyState;
	
			function checkReadyState() {
				if (reader.readyState === 4) {
					//check to see whether request for the file failed or succeeded
					if ((reader.status == 200) || (reader.status == 0)) {
					   var url_string = "https://bmkg-content-inatews.storage.googleapis.com/mt." + feature.properties.id + ".png";
					}
					else {
					   var url_string = "/assets/no_mt.png";
					}
				}
				var popupContent = "<p>OT (UTC) : " + feature.properties.time + "</br>Longitude : " + parseFloat(feature.geometry.coordinates[0]).toFixed(2) + "</br>Latitude : " + parseFloat(feature.geometry.coordinates[1]).toFixed(2) + "</br>Magnitude : " + parseFloat(feature.properties.mag).toFixed(1).toString() + "</br>Depth : " + parseFloat(feature.properties.depth).toFixed(0).toString() + " Km</br>Location : " + feature.properties.place + "</br>Focal Mechanism : <img src=" + url_string + " style='width:100px;'></p>";
				layer.bindPopup(JSON.stringify(popupContent).replace(/"/g, ''))
			}
			reader.send(null);
        },
    },
});

// Latest earthquake marker
var eqIcon = L.icon({
	iconUrl: '/assets/gempa.gif',
	iconSize: [70, 70], // size of the icon
});

window.myLatestEq = Object.assign({}, window.myLatestEq, {  
    myMarkerLatestEq: {  
		pointToLayer: function (feature, latlng) {
			return L.marker(latlng, {
				icon: eqIcon
			});
		},
		bindPopup: function(feature, layer) {
			var reader = new XMLHttpRequest();
			var checkFor = "https://bmkg-content-inatews.storage.googleapis.com/mt." + feature.properties.id + ".png";
			reader.open('get', checkFor, true);
			reader.onreadystatechange = checkReadyState;
	
			function checkReadyState() {
				if (reader.readyState === 4) {
					//check to see whether request for the file failed or succeeded
					if ((reader.status == 200) || (reader.status == 0)) {
					   var url_string = "https://bmkg-content-inatews.storage.googleapis.com/mt." + feature.properties.id + ".png";
					}
					else {
					   var url_string = "/assets/no_mt.png";
					}
				}
				var popupContent = "<p>OT (UTC) : " + feature.properties.time + "</br>Longitude : " + parseFloat(feature.geometry.coordinates[0]).toFixed(2) + "</br>Latitude : " + parseFloat(feature.geometry.coordinates[1]).toFixed(2) + "</br>Magnitude : " + parseFloat(feature.properties.mag).toFixed(1).toString() + "</br>Depth : " + parseFloat(feature.properties.depth).toFixed(0).toString() + " Km</br>Location : " + feature.properties.place + "</br>Focal Mechanism : <img src=" + url_string + " style='width:100px;'></p>";
            	layer.bindPopup(JSON.stringify(popupContent).replace(/"/g, ''))
			}
			reader.send(null);
        },
    },
});


// Slab Color
function getColorSlab(d) {
	return d < 20 ? '#E80712' :
		d < 40 ? '#EB2712' :
		d < 60 ? '#EE3A19' :
		d < 80 ? '#F14D1F' :
		d < 100 ? '#F35A1F' :
		d < 120 ? '#F56724' :
		d < 140 ? '#F77227' :
		d < 160 ? '#FA802B' :
		d < 180 ? '#FA8D33' :
		d < 200 ? '#FA9A3A' :
		d < 220 ? '#FDA740' :
		d < 240 ? '#FDB445' :
		d < 260 ? '#FDC149' :
		d < 280 ? '#FBD160' :
		d < 300 ? '#FDDC56' :
		d < 320 ? '#FDEA5A' :
		d < 340 ? '#FAF560' :
		d < 360 ? '#F5F767' :
		d < 380 ? '#E9F16C' :
		d < 400 ? '#DFE876' :
		d < 420 ? '#D3E17C' :
		d < 440 ? '#CADC84' :
		d < 460 ? '#BFD389' :
		d < 480 ? '#B5CF90' :
		d < 500 ? '#A8C795' :
		d < 520 ? '#A0C29D' :
		d < 540 ? '#91BAA1' :
		d < 560 ? '#86B5A7' :
		d < 580 ? '#79ADAB' :
		d < 600 ? '#6BA9B4' :
		d < 620 ? '#5DA3B8' :
		d < 640 ? '#4F9EBD' :
		d < 660 ? '#51A2C7' :
		d < 680 ? '#389BCC' :
					'#000000';
}

// Plate Tectonic style

window.myTectonic = Object.assign({}, window.myTectonic, {  
	myTrench: {  
		style: function(feature) {  
			return {
				color: 'red',
				weight: 2
			}; 
        	}, 			
		
        	bindPopup: function(feature, layer) {
			var popupContent = "<p>" + feature.properties["TRENCH"] + "</p>";
			layer.bindPopup(JSON.stringify(popupContent).replace(/"/g, ''))
		},
	},
	myTransform: {  
		style: function(feature) {  
			return {
				color: 'black',
				weight: 2
			}; 
        	}, 			
		
        	bindPopup: function(feature, layer) {
			var popupContent = "<p>" + feature.properties["TRANSFORM"] + "</p>";
			layer.bindPopup(JSON.stringify(popupContent).replace(/"/g, ''))
		},
	},
	myRidge: {  
		style: function(feature) {  
			return {
				color: 'blue',
				weight: 2
			}; 
        	}, 			
		
        	bindPopup: function(feature, layer) {
			var popupContent = "<p>" + feature.properties["RIDGE"] + "</p>";
			layer.bindPopup(JSON.stringify(popupContent).replace(/"/g, ''))
		},
	},
	myFault: {  
		style: function(feature) {  
			return {
				color: 'brown',
				weight: 2
			}; 
        	}, 			
	},
	mySlab: {
		style: function(feature) {  
			return {
				color: getColorSlab(feature.properties.DEPTH),
				weight: 2
			}; 
        	}, 	
	    bindPopup: function(feature, layer) {
			var popupContent = "<p>Depth : " + feature.properties["DEPTH"] + " Km</br>Region : " + feature.properties["REGION"] + "</p>";
			layer.bindPopup(JSON.stringify(popupContent).replace(/"/g, ''))
		},		
	},
});
