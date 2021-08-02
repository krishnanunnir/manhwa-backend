import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
  Dropdown,
  DropdownItem,
  DropdownToggle,
  DropdownMenu,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      title: "",
      description: "",
      author: "",
      status: "Ongoing",
      dropdown: false,
    };
  }

  handleChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };
  handleDropdodwn() {
    this.state.dropdown = !this.state.dropdown;
  }

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Add a missing Manhwa</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="manhwaTitle">Title</Label>
              <Input
                type="text"
                id="manhwaTitle"
                name="title"
                value={this.state.title}
                onChange={this.handleChange}
                placeholder="Enter Manhwa Title"
              />
            </FormGroup>
            <FormGroup>
              <Label for="manhwaAuthor">Author</Label>
              <Input
                type="text"
                id="manhwaAuthor"
                name="author"
                value={this.state.author}
                onChange={this.handleChange}
                placeholder="Enter Manhwa Author"
              />
            </FormGroup>
            <FormGroup>
              <Label for="manhwaDescription">Description</Label>
              <Input
                type="textarea"
                id="manhwaDescription"
                name="description"
                value={this.state.description}
                onChange={this.handleChange}
                placeholder="Enter Manhwa description"
              />
            </FormGroup>
          </Form>
          <Dropdown isOpen={this.state.dropdown} toggle={this.handleDropdodwn}>
            <DropdownToggle caret>Status</DropdownToggle>
            <DropdownMenu right>
              <DropdownItem header>Ongoing</DropdownItem>
              <DropdownItem disabled>Cancelled</DropdownItem>
              <DropdownItem>Completed</DropdownItem>
            </DropdownMenu>
          </Dropdown>
        </ModalBody>
        <ModalFooter>
          <Button color="success" onClick={() => onSave(this.state.activeItem)}>
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}
