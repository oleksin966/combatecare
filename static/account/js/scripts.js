$('#cart-link').click(function(e) {
    e.preventDefault();
    $('#cart-modal').modal('show');
});
    
function updateCart() {
  fetch(`/cart/`)
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('cart-items');
      const cartCounter = document.getElementById('cart-counter');
      const span = document.createElement('span');
      container.innerHTML = '';
      data.cart_items.forEach(item => {
        //console.log(data.cart_items.length)
        const element = document.createElement('tr');
        element.innerHTML = `
          <td><img src="${item.photo}" alt="${item.name} photo" width="100" height="100"></td>
          <td><p class="item-name">${item.name}</p></td>
          <td>
            <form action="/cart/update/${item.id}/" method="post">
              <input type="number" data-item-id="${item.id}" class="quantity-input" name="quantity_${item.id}" value="${item.quantity}" min="1" max="${item.max_quantity}" class="form-control">
            </form>
          <td>
          <form action="/cart/remove/${item.id}/" method="post">
          <button type="submit" data-item-id="${item.id}" class="remove-from-cart-btn btn btn-danger btn-sm">Видалити</button>
          </form>
          </td>`;
        container.appendChild(element);
      });
        span.innerHTML = data.cart_items.length;
        cartCounter.innerHTML = '';
        cartCounter.appendChild(span);
    });
}


window.addEventListener('load', updateCart);

document.addEventListener('click', event => {
  if (event.target.classList.contains('add-to-cart-btn')) {
    const itemId = event.target.dataset.itemId;
    fetch(`/cart/add/${itemId}`)
      .then(response => response.json())
      .then(data => {
        console.log(data)
        if (data.message === 'ok') {
          updateCart();
        }
      });
  } else if (event.target.classList.contains('remove-from-cart-btn')) {
    event.preventDefault(); 
    const itemId = event.target.dataset.itemId;
    fetch(`/cart/remove/${itemId}`)
      .then(response => response.json())
      .then(data => {
        if (data.message === 'ok') {
          updateCart();
        }
      });
  } 
});


document.addEventListener('input', event => {
  if (event.target.name.startsWith('quantity_')) {
    const itemId = event.target.name.replace('quantity_', '');
    const newQuantity = event.target.value;
    console.log(newQuantity)
    const csrftoken = getCookie('csrftoken');
    fetch(`/cart/update/${itemId}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body: JSON.stringify({quantity: newQuantity})
    })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'ok') {
          updateCart();
        }
      });
    }
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.7749, lng: -122.4194},
    zoom: 8
  });
}