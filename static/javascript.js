function search_movie() {

    var query = document.getElementById("q").value;

    if (query === "")
    {
        let list = document.querySelector('#result');
        list.innerHTML = "";
        return;
    }
        
    
    fetch(`${window.origin}/search`, {
        method: "POST",
        body: JSON.stringify(query),
        headers: new Headers({
            "content-type": "application/json"
        })
    })
    .then(function(response) {

        if (response.status !== 200)
        {
            console.log(`Error ${resonse.status}`);
            return;
        }

        response.json().then(function(data){
            let list = document.querySelector('#result');

            let out = "";

            for (let movie of data){

                out += `
                    <li>${movie.title}</li>
                `
            }

            list.innerHTML = out;
        })
    })
}