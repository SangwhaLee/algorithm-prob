/* 
  아래에 코드를 작성해주세요.
*/
const searchInput = document.querySelector(".search-box__input")
const searchResult = document.querySelector(".search-result")
const searchBtn = document.querySelector(".search-box__button")

function fetchAlbums(page=1, limit=10){
  const keyword = searchInput.value
  const API_URI = `http://ws.audioscrobbler.com/2.0/?method=album.search&album=${keyword}&limit=${limit}&page=${page}&api_key=1de14c2813b051d25b3d0d660a7ece68&format=json`
  axios.get(API_URI)
    .then((response) => {
      // console.log(response.data.results.albummatches.album)
      albums = response.data.results.albummatches.album
      for(let i=0;i<limit;i++){
        const card = document.createElement("div")
        card.classList.add("search-result__card")
        const cardText = document.createElement("div")
        cardText.classList.add("search-result__text")
        const cardImg = document.createElement("img")
        cardImg.src = albums[i].image[1]['#text']
        card.appendChild(cardImg)
        const artistName = document.createElement("h2")
        const albumName = document.createElement("p")
        artistName.innerText = albums[i].artist
        albumName.innerText = albums[i].name
        cardText.appendChild(artistName)
        cardText.appendChild(albumName)
        card.appendChild(cardText)
        searchResult.append(card)
      }
    })
    .catch((response) => {
      alert("잠시 후 다시시도해주세요")
    })
}

searchBtn.addEventListener("click", fetchAlbums)
