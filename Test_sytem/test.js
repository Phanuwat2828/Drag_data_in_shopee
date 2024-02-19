const apiUrl = 'https://www.lazada.co.th/?spm=a2o4m.home-th.header.dhome.47fb7f6dgHALgf'; // Replace with the actual API URL

fetch(apiUrl + '/some/endpoint', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    // Add any other required headers here
  },
  // Add any other options such as credentials, mode, etc.
})
  .then(response => response.json())
  .then(data => {
    console.log('API Response:', data);
  })
  .catch(error => {
    console.error('Error:', error);
  });