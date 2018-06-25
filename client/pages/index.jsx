import { StrictMode, Component } from 'react';
import { render } from 'react-dom';

import dynamic from 'next/dynamic'

const Map = dynamic(import('../components/Map'), {
  ssr: false,
});


const pointEqual = (p1, p2) => {
  if (p1 == null || p2 == null) {
    return false;
  }

  const [x1, y1] = p1;
  const [x2, y2] = p2;

  return (x1 === x2) && (y1 === y2);
};


export default class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      start: null,
      end: null,
      path: null,
    }
  }
  handleClick(lat, lng) {
    const {start, end} = this.state;

    this.setState({
      start: start || [lat, lng],
      end: (start && !end) ? [lat, lng] : end,
    });

    // this.setState({
    //   start: [-12.065236650836018, -77.0682978630066],
    //   end: [-12.072098225470006, -77.06404924392702],
    // })

    console.log(lat, lng);
  }
  async componentDidUpdate(prevProps, prevState) {
    const {start: prevStart, end: prevEnd} = prevState;
    const {start, end} = this.state;
    if (!(pointEqual(prevStart, start) && pointEqual(prevEnd, end))
      && start
      && end
    ) {
      const res = await fetch('http://localhost:5000/route', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          start,
          end,
        }),
      });

      const {path} = await res.json();
      if (pointEqual(this.state.start, start) && pointEqual(this.state.end, end)) {
        this.setState({ path });
      }
    }
  }
  handleContextMenu() {
    this.setState({
      start: null,
      end: null,
      path: null,
    });
  }
  render() {
    return (
      <StrictMode>
        <Map
          center={[-12.072071, -77.080393]}
          onClick={({latlng: {lat, lng}}) => this.handleClick(lat, lng)}
          onContextMenu={({latlng: {lat, lng}}) => this.handleContextMenu(lat, lng)}
          line={this.state.path || []}
          />
      </StrictMode>
    );
  }
}
