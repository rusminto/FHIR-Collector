const Client = require('fhir-kit-client');
const fhirClient = new Client({
//  baseUrl: 'https://r4.test.pyrohealth.net/fhir'
  baseUrl: 'http://localhost:3000'
  });

// Get SMART URLs for OAuth
fhirClient.smartAuthMetadata().then((response) => {
  console.log(response);
  });

// Search for patients, and page through results
fhirClient
  .search({ resourceType: 'Patient', searchParams: { _count: '10' } })
  .then((response) => {
    console.log(response);
    return response;
  })
  .catch((error) => {
    console.error(error);
  });
