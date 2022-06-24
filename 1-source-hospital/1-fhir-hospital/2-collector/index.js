const Client = require('fhir-kit-client');
const fhirClient = new Client({
    baseUrl: 'https://r4.test.pyrohealth.net/fhir'
});
const axios = require('axios').default;

// Get SMART URLs for OAuth
fhirClient.smartAuthMetadata().then((response) => {
    console.log(response);
});

// Search for patients, and page through results
fhirClient
  .search({ resourceType: 'Patient', searchParams: { _count: '10' } })
  .then( async(response) => {
    
    await axios.post('http://localhost:3001/Patient', response)
    .then(function (response) {
        console.log(response);
    })
    .catch(function (error) {
        console.log(error);
    });

    return response;
  })
  .catch((error) => {
    console.error(error);
  });
