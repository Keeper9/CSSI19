let counter = 1;

function addClass()
{
    let value = document.forms['tester']['newelement'].value;
	document.forms['tester']['newelement'].value = "";
	
    if(value != "")
    {
		let parent = document.createElement('div');
        let label = document.createElement('label');
        let input = document.createElement('input');
       
        input.name = "class" + counter;
        counter += 1;
        input.type = "text";
        label.for = input.name;
        label.innerHTML = value + ": ";
		
		parent.appendChild(label);
        parent.appendChild(input);
		
        document.forms['tester'].insertBefore(parent,document.forms['tester']['submit']);
    }

}