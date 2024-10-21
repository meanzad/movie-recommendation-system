function search_movie() {

    var query = document.getElementById("q").value;
    
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
            let table = document.querySelector('#result');

            let out = "";

            for (let movie of data){

                out += `
                    <tr>
                        <td>${movie.movieId}</td>
                        <td>${movie.title}</td>
                    </tr>
                
                `
            }

            table.innerHTML = out;
        })
    })
}