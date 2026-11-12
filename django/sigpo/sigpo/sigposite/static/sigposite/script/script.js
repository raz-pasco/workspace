document.addEventListener('DOMContentLoaded', function() {
	document.getElementById('livre_all').onchange = check_all_livre ;
	document.getElementById('paye_all').onchange = check_all_paye ;
});

/*		alert(`debug if !!${max}`);
		alert('debug else !!');
*/

// ========== fill id paye  / uncheck checkbox all ========== //
function check_id_livre(i){
	document.getElementById(`id_form-${i}-quantite`).value++;
}

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
	let val = document.getElementById(`_id_${i}`).value ;
	if (document.getElementById(`paye_${i}`).checked == true){
		document.getElementById(`paye_id_${i}`).value = val;
	}
	else{
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
