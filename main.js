const arcgisMapId = '1c365daf37a744fbad748b67aa69dac8'; 
const arcgisApiKey = config.ARCGIS_API_KEY;

const map = new maplibregl.Map({
  container: "map",
  style: `https://basemaps-api.arcgis.com/arcgis/rest/services/styles/${arcgisMapId}?type=style&token=${arcgisApiKey}`,
  zoom: 2,
  center: [-118.805, 34.027]
});