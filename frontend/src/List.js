import React, { Component } from "react";
import axios from "axios";
import Manhwa from "./components/Manhwa";
import { Alert } from "reactstrap";
import "./Home.css";
import "./Manhwa.css";
class Home extends Component {
  constructor(props) {
    super(props);
    this.addActiveManhwa = this.addActiveManhwa.bind(this);
    const {
      params: { listSlug },
    } = props.match;
    this.listSlug = listSlug;
    this.state = {
      title: "",
      identifier: "",
      manhwaList: [],
      activeManhwa: [],
    };
  }
  componentDidMount() {
    this.refreshList();
    this.setState({
      activeManhwa:
        localStorage.getItem("activeManhwa") != null
          ? JSON.parse(localStorage.getItem("activeManhwa"))
          : [],
    });
  }

  refreshList = () => {
    axios.get("/api/list/" + this.listSlug).then((res) =>
      this.setState({
        manhwaList: res.data.manhwas,
        title: res.data.title,
        identifier: res.data.identifier,
      })
    );
  };
  fetchData = () => {
    axios.get(this.state.next).then((res) => {
      var has_more = false;
      if (res.data.next) {
        has_more = true;
      }
      var data = {
        next: res.data.next,
        manhwaList: this.state.manhwaList.concat(res.data.results),
        more_exist: has_more,
      };
      this.setState(data);
    });
  };

  manhwaModalToggle = () => {
    this.setState({ newManhwaModal: !this.state.newManhwaModal });
  };
  clearList = () => {
    localStorage.removeItem("activeManhwa");
    this.setState({
      activeManhwa: [],
    });
    window.location.reload();
  };
  listModalToggle = () => {
    this.setState({ listModal: !this.state.listModal });
  };
  handleListModalSubmit = (data) => {
    this.listModalToggle();
  };

  handleManhwaModalSubmit = (item) => {
    this.manhwaModalToggle();
    const formData = new FormData();
    for (var key in item) {
      formData.append(key, item[key]);
    }
    axios({
      method: "post",
      url: "/api/manhwa/",
      data: formData,
      headers: {
        "Accept-Language": "en-US,en;q=0.8",
        "Content-Type": `multipart/form-data`,
      },
    });
  };
  handleListModalSubmit = (item) => {
    item = { ...item, manhwas: this.state.activeManhwa };
    axios({
      method: "post",
      url: "/api/list/",
      data: JSON.stringify(item),
      headers: {
        accept: "application/json",
        "Accept-Language": "en-US,en;q=0.8",
        "Content-Type": `application/json`,
      },
    });
  };

  addActiveManhwa = (manhwa) => {
    const index = this.state.activeManhwa.indexOf(manhwa);
    var activeManhwa = this.state.activeManhwa;
    if (index > -1) {
      activeManhwa.splice(index, 1);
    } else {
      activeManhwa = [...activeManhwa, manhwa];
    }
    this.setState({ activeManhwa: activeManhwa }, () => {
      localStorage.setItem(
        "activeManhwa",
        JSON.stringify(this.state.activeManhwa)
      );
    });
  };

  render() {
    return (
      <main className="container">
        <div className="row justify-content-center m-24 manhwaMargintitle">
          <div className="col-md-6 col-md-offset-3">
            <h1>{this.state.title}</h1>
          </div>
        </div>
        <div className="mb-24">
          <div className="row justify-content-center">
            <div className="col-md-6 col-md-offset-3">
              <p>
                <i>Created by</i> <strong>{this.state.identifier}</strong>
              </p>
            </div>
          </div>
        </div>
        <div class="row justify-content-center mt-8">
          <div className="col-md-6 col-md-offset-3">
            <Alert color="primary">
              <p>You can share this list by copying this url!</p>
              <p>{window.location.href}</p>
            </Alert>
          </div>
        </div>
        <div>
          {this.state.manhwaList.map((item) => (
            <Manhwa
              key={item.id}
              item={item}
              selected={this.state.activeManhwa.includes(item.slug)}
              onChange={this.addActiveManhwa}
            />
          ))}
        </div>
      </main>
    );
  }
}

export default Home;
