# AirBnB Clone Project

This project is an implementation of an AirBnB clone, which includes a command-line interface to manage AirBnB objects. The command interpreter allows users to create, retrieve, update, and delete objects within the AirBnB system.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Ubuntu 20.04 LTS (or any compatible environment)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/AirBnB_clone.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AirBnB_clone
    ```

3. Run the command interpreter:

    ```bash
    ./console.py
    ```

## Usage

Once inside the command interpreter, you can use various commands to interact with AirBnB objects:

- `help`: Display a list of available commands and their descriptions.
- `create`: Create a new instance of a specified AirBnB object.
- `show`: Display details of a specific instance based on its ID.
- `update`: Update attributes of a specified instance.
- `destroy`: Delete a specified instance.
- `all`: Display details of all instances or of a specific class.
- `quit` or `EOF`: Exit the command interpreter.

## Examples

Here are some examples of using the command interpreter:

```bash
(hbnb) help
```

```bash
(hbnb) create User
```

```bash
(hbnb) show User f0f6c342-42d4-4e15-a16e-1bb6f6fc24a1
```

```bash
(hbnb) update User f0f6c342-42d4-4e15-a16e-1bb6f6fc24a1 name "John Doe"
```

```bash
(hbnb) all
```

## Authors

- [Salma Saeed](https://github.com/salmasaeed12)

## Branches and Pull Requests

We use branches and pull requests extensively on GitHub to organize our work and collaborate effectively. Each feature or bug fix is developed in its own branch, and pull requests are created to merge changes into the main branch after review.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
