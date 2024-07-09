document.addEventListener('DOMContentLoaded', function() {
    var searchButton = document.querySelector('#search-btn');
    var searchForm = document.querySelector('.search-form');

    searchButton.addEventListener('click', function() {
        searchForm.classList.toggle('active');
    });
});

window.onscroll = () => {
    searchForm.classList.remove('active');

    if (window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    }
    else {
        document.querySelector('.header .header-2').classList.remove('active');
    }
}

window.onload =()=> {
    if (window.scrollY>80) {
        document.querySelector('.header .header-2').classList.add('active');
    }
    else {
        document.querySelector('.header .header-2').classList.remove('active');
    }
}