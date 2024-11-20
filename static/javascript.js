function selectInput(select) {

    var query = document.getElementById("q");
    query.value = select.getElementsByTagName('span')[0].innerHTML;
    var queryid = document.getElementById("queryId");
    queryid.value = select.getElementsByTagName('input')[0].value;
    let list = document.querySelector('#result');
    list.innerHTML = "";
    return;
}


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
                    <li onclick="selectInput(this)">
                    <span>${movie.title}</span>
                    <input type='hidden' value="${movie.movieId}">
                    </li>
                `
            }

            list.innerHTML = out;
        })
    })
}

function validateForm() {
    var x = document.forms["movie-form"]["movieId"].value;
    if (x == "") {
      alert("Please select a movie from the list");
      return false;
    }
  }
  


