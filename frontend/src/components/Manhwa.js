import React, { Component } from "react";
import { Link } from "react-router-dom";
import plus from "./rounded-plus.svg";
import minus from "./rounded-minus.svg";

class Manhwa extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selected: this.props.selected,
    };
  }
  handleChange = (item) => {
    const { onChange } = this.props;
    this.setState({ selected: !this.state.selected });
    onChange(item.slug);
  };
  render() {
    const { item } = this.props;
    this.selected = this.state.selected ? "activeManhwa" : "";
    this.icon = this.state.selected ? minus : plus;
    return (
      <div className="manhwaMargin">
        <div className="row justify-content-center">
          <div
            className={`col-md-6 col-md-offset-3 d-flex flex-row ${this.selected}`}
          >
            <div className="d-flex flex-column  justify-content-center">
              <img
                src={item.cover_image}
                alt={item.description}
                style={{
                  height: "auto",
                  width: "auto",
                  maxHeight: "7em",
                  maxWidth: "7em",
                }}
              />
            </div>
            <div>
              <div className="d-flex flex-column p-4">
                <h5>
                  <Link to={`manhwa/${item.slug}`}>{item.title} </Link>
                  <img
                    src={this.icon}
                    className="img-fluid"
                    alt="logo"
                    onClick={() => {
                      this.handleChange(item);
                    }}
                  />
                </h5>
                <p className="pt-2">{item.description} </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Manhwa;
