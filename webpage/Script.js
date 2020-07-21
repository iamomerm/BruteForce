function Authenticate()
{
	let Username = document.getElementById('Username').value; /* Username */

	let Password = document.getElementById('Password').value; /* Password */

	if ((Username == 'admin') && (Password == 'admin'))
	{
		document.getElementById('Sheet').style = "font-size: 45px; color: green";
		document.getElementById('Error').innerHTML = '';
		document.getElementById('Sheet').innerHTML = 'Success! :)';
	}

	else
	{
		PW = document.getElementById('Password').value;		
		document.getElementById('Password').value = '';
		document.getElementById('Error').innerHTML = 'Wrong password - ' + PW;
	}

}
