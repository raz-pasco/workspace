document.addEventListener('DOMContentLoaded', function() {
//	document.getElementById('ticket').onclick = ticket_caisse ;
	document.getElementById('espece').onkeyup = calcul_rendu ;
	document.getElementById('livre_all').onchange = check_all_livre ;
	document.getElementById('paye_all').onchange = check_all_paye ;
});

/*
		alert(`debug if !!${max}`);
		alert('debug else !!');
*/

// ========== ticket de caisse ========== //
function ticket_caisse(table){
	let form = document.getElementById('form');
	let esp = document.getElementById('espece').value;
	let url = `../ticket/${table}?espece=${esp}`;
//	alert(`debug if !!${esp}`);
	window.open(url, '_blank');
	setTimeout(() => { form.submit(); }, 500);
}
// ======================================= //

// ========== paiement rendu ========== //
function calcul_rendu(){
	let espece=document.getElementById('espece');
	let net=document.getElementById('net');
	let rendu=document.getElementById('rendu');
	let n = parseInt(net.value);
	let e = parseInt(espece.value);
	if(parseInt(espece.value) >= parseInt(net.value) && parseInt(espece.value) > 0 ){
		rendu.value = e - n;
	}
	else{
		rendu.value = 0;
	}
}

// =================================== //
// ========== alpha visible  ========== //
/*var $scrollingDiv = $("#scrollingDiv"); 
$(window).scroll(function(){ 
	if ($(window).scrollTop()>220) { 
		$scrollingDiv
			.css("position",'fixed' )
			.css("top",'46px' )
	}
	else {
		$scrollingDiv 
			.css("position",'' )
			.css("top",'' ) 
	}
})*/;
// ========== button moins  ========== //
function bt_plus(i){
	let qte = document.getElementById(`id_form-${i}-quantite`);
	qte.value++;
}

// ========== button moins  ========== //
function bt_moins(i){
	let qte = document.getElementById(`id_form-${i}-quantite`);
	if ( qte.value > 0 ){
		qte.value-- ;
	}
	else{
		alert('0 ou plus uniquement !!');
//		document.getElementById(`livre_id_${i}`).value = '' ;
//		document.getElementById(`livre_all`).checked = false;
	}
}

// ========== confirme new commande ========== //
function confirm_new_commande(){
	max = "ici !!";
	alert(`debug if !!${max}`);
	document.write("<h1>Hello World</h1><form action=\"{% url 'confirmer' table_id %}\" method=\"post\" >{% csrf_token %}<table>{{ formset }}</table><input type=\"button\" id=\"bt_cmd\" name=\"bt_cmd\" value=\"Inserer\"/><input type=\"submit\" value=\"Ajouter\"/>{{ add }}</form>");
}

// ========== fill id paye  / uncheck checkbox all ========== //
/*function check_id_livre(i){
	document.getElementById(`id_form-${i}-quantite`).value++;
}*/

// ========== fill id paye  / uncheck checkbox all ========== //
function check_id_livre(i){
	let val = document.getElementById(`_id_${i}`).value ;
	if (document.getElementById(`livre_${i}`).checked == true){
		document.getElementById(`livre_id_${i}`).value = val ;
	}
	else{
		document.getElementById(`livre_id_${i}`).value = '' ;
		document.getElementById(`livre_all`).checked = false;
	}
}

// ========== fill id paye  / uncheck checkbox all ========== //
function check_id_paye(i){
	let val = parseInt(document.getElementById(`_id_${i}`).value) ;
	let mnt = parseInt(document.getElementById(`_montant_${i}`).value) ;
	let net = parseInt(document.getElementById(`net`).value) ;
	if (document.getElementById(`paye_${i}`).checked == true){
		document.getElementById(`paye_id_${i}`).value = val;
		document.getElementById(`montant_${i}`).value = mnt;
		document.getElementById(`net`).value = net + mnt;
//		document.getElementById(`espece`).placeholder = net + mnt;
	}
	else{
//		document.getElementById(`espece`).placeholder = net - mnt;
		document.getElementById(`net`).value = net - mnt;
		document.getElementById(`montant_${i}`).value = 0;
		document.getElementById(`paye_id_${i}`).value = '' ;
		document.getElementById(`paye_all`).checked = false;
	}
}

// ========== check / uncheck all checkbox payé ========== //
function check_all_paye(){
	let max = document.getElementById('max').value;
	if (document.getElementById('paye_all').checked == true){
		for ( i = 0 ; i < max ; i++ ){
			document.getElementById(`paye_id_${i}`).value = document.getElementById(`_id_${i}`).value;
			document.getElementById(`paye_${i}`).checked = true;
		}
	}
	else{
		for ( i = 0 ; i < max ; i++ ){
			document.getElementById(`paye_id_${i}`).value = '' ;
			document.getElementById(`paye_${i}`).checked = false;
		}
	}
}

// ========== check / uncheck all checkbox livré ========== //
function check_all_livre(){
	let max = document.getElementById('max').value;
	if (document.getElementById('livre_all').checked == true){
		for ( i = 0 ; i < max ; i++ ){
			document.getElementById(`livre_id_${i}`).value = document.getElementById(`_id_${i}`).value;
			document.getElementById(`livre_${i}`).checked = true;
		}
	}
	else{
		for ( i = 0 ; i < max ; i++ ){
			document.getElementById(`livre_id_${i}`).value = '' ;
			document.getElementById(`livre_${i}`).checked = false;
		}
	}
}

function fill( form, field ){
	alert('form:'+form+'field:'+field);
//	document.forms["newCommande"][name].value++;
}
