import React, { Component } from 'react';
class Manhwa extends Component {
    render() {
      return (
        <div className="manhwa">
        <div className="row justify-content-center">
          <div className="col-md-6 col-md-offset-3 d-flex flex-row">
            <div className="d-flex flex-column  justify-content-center">
              <img src={this.props.item.cover_image} alt={this.props.item.description} />
            </div>
            <div>
              <div className="d-flex flex-column p-4">
                <h5>{this.props.item.title} </h5>
                <p className="pt-2">{this.props.item.description} </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      );
    }
  }

  export default Manhwa;