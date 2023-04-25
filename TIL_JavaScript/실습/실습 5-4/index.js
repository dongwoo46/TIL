/* 
  아래에 코드를 작성해주세요.
*/
//https://ws.audioscrobbler.com/2.0/?method=album.search&album=kitch&api_key=66f4ac45c4892c8fe6d02dff77cabc5c&format=json
//66f4ac45c4892c8fe6d02dff77cabc5c
const API_KEY = '66f4ac45c4892c8fe6d02dff77cabc5c'
const searchBtn = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')
const inputTag = document.querySelector('.search-box__input')

// function fetchAlbums() {} 이렇게 쓰면 괄호 필요 없음
//밑의 방식으로 쓰면 괄호가 필요
const fetchAlbums = function() { 
  // 리턴값으로 아래 값들을 호출하겠다.
  return () => {
    const keyword = document.querySelector('.search-box__input').value
    console.log(keyword)
    axios({
      method :'get',
      url : 'https://ws.audioscrobbler.com/2.0',
      params: {
        method : 'album.search',
        album : keyword,
        api_key : API_KEY,
        format : 'json'
      }
    }).then(result => {
      console.log(result)
    }).catch(()=>alert('에러'))
  }
}

searchBtn.addEventListener('click', fetchAlbums())

const divTag = document.createElement('div')
divTag.classList.add('search-result__card')
document.body.appendChild(divTag)

const imgTag = document.createElement('img');
divTag.appendChild(imgTag);
imgTag.setAttribute('src', 'https://lastfm.freetls.fastly.net/i/u/174s/bd13a8e1d9c8885133970d7592c88b2d.png');

const divResult = document.createElement('div');
divResult.classList.add('search-result__text');
const h2 = document.createElement('h2');
const pTag = document.createElement('p');

h2.innerText = '아티스트의 이름';
pTag.innerText = '앨범의 이름';
divResult.appendChild(h2);
divResult.appendChild(pTag);
divTag.appendChild(divResult);