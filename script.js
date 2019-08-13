let counter = 1;

function addClass()
{
    let value = document.forms['tester']['newclass'].value;

    if(value != "")
    {
        let label = document.createElement('label');
        let child = document.createElement('input');
       
        child.name = "class" + counter;
        counter += 1;
        chlid.type = "text";
        label.for = child.name;
        label.innerHTML = value; 
        label.appendChild(child);

        document.insertBefore(label,document.forms['tester']['submit']);
    }

}