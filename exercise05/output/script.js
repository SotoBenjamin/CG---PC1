const kernel_size = [3,5,7,9,11,13,15,17,19,21,23,25]

//format of img : filter_type_kernelsize.png

const rows = [
  {filter : 'box' , type : 'gray' , label : 'Box-Gray'},
  {filter : 'box' , type : 'rgb' , label : 'Box-RGB'},
  {filter : 'bartlett' , type : 'gray' , label : 'Bartlett-Gray'},
  {filter : 'bartlett' , type : 'rgb' , label : 'Bartlett-RGB'},
  {filter : 'gaussian' , type : 'gray' , label : 'Gaussian-Gray'},
  {filter : 'gaussian' , type : 'rgb' , label : 'Gaussian-RGB'},
]


function create_carousel(filter , type){
  const visible_count = 3;
  const n_group = Math.ceil(kernel_size.length / visible_count);
  const max_index = n_group -1
  let c = 0;
  const carousel_item_width = 300;
  const carousel_item_margin = 20;
  const advance_next_group = (carousel_item_width + carousel_item_margin)*visible_count;

  const carousel_window = document.createElement('div');
  carousel_window.className = 'carousel-window';
  const carousel_track = document.createElement('div');
  carousel_track.className = 'carousel-track';
  for(let  i = 0 ; i < kernel_size.length ; i++){
      const k = kernel_size[i];
      const item = document.createElement('div');
      item.className = 'carousel-item';
      const label = document.createElement('div');
      label.className = 'kernel-label';
      label.textContent = `${k}x${k}`;
      const img = document.createElement('img');
      img.className = 'carousel-img';
      img.src       = `${filter}_${type}_${k}.png`;
      item.appendChild(label);
      item.appendChild(img);
      carousel_track.appendChild(item);
  }
  carousel_window.appendChild(carousel_track);


  const button_prev = document.createElement('button');
  button_prev.className = 'carousel-prev';
  button_prev.innerText = '<';
  button_prev.addEventListener('click' , ()=>{
      c = c > 0 ? c - 1: max_index
      carousel_track.style.transform = `translateX(-${c * advance_next_group}px)`;
  });

  const button_next = document.createElement('button');
  button_next.className = 'carousel-next';
  button_next.innerText = '>';
  button_next.addEventListener('click' , () => {
    c = c < max_index ? c+1 : 0;
    carousel_track.style.transform = `translateX(-${c * advance_next_group}px)`;
  });

  const carousel = document.createElement('div');
  carousel.className = 'carousel';
  carousel.appendChild(button_prev);
  carousel.appendChild(carousel_window);
  carousel.appendChild(button_next);

  return carousel;
}

function create_table(){
  const table = document.getElementById('filter-table');
  const thead = table.createTHead();
  const head_row = thead.insertRow();
  head_row.insertCell().textContent = 'Filter-type';
  head_row.insertCell().textContent = 'Originals'
  head_row.insertCell().textContent = 'Filters';
  const tbody = table.createTBody();
  for(let i = 0 ; i < rows.length ; i++){
    const {filter,type,label} = rows[i];
    const tr = tbody.insertRow();

    const th = document.createElement('th');
    th.textContent = label;
    tr.appendChild(th);
    
    let td = tr.insertCell();
    const original_img = document.createElement('img');
    original_img.className = 'orig-img';
    original_img.src  = `original_${type}.png`;
    td.appendChild(original_img);
    td = tr.insertCell();
    td.appendChild(create_carousel(filter, type));
  }

  //fila especial para laplaciano
  const trExtra = tbody.insertRow();

  const thExtra = document.createElement('th');
  thExtra.textContent = 'Laplacian';
  trExtra.appendChild(thExtra);

  let tdOrig = trExtra.insertCell();
  const imgOrigGray = document.createElement('img');
  imgOrigGray.className = 'orig-img';
  imgOrigGray.src = 'original_gray.png';
  tdOrig.appendChild(imgOrigGray);

  let tdFilt = trExtra.insertCell();

  const imgLap3 = document.createElement('img');
  imgLap3.className = 'orig-img';
  imgLap3.src    = 'laplacian3.png';
  imgLap3.style.marginRight = '10px';   
  tdFilt.appendChild(imgLap3);

  const imgLap5 = document.createElement('img');
  imgLap5.className = 'orig-img';
  imgLap5.src    = 'laplacian5.png';
  imgLap5.alt    = 'laplacian5.png';
  tdFilt.appendChild(imgLap5);
}

document.addEventListener('DOMContentLoaded',create_table);