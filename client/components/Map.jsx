import { Map, TileLayer, Polyline } from 'react-leaflet';

export default ({children, line, ...props}) => (
  <Map zoom={17} style={{
         height: '100vh',
         width: '100%',
       }}
       {...props}
     >
    <TileLayer
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
      />
    <Polyline
      positions={line}
    />
    {children}
  </Map>
);
