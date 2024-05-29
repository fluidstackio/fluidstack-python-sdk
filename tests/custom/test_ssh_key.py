def test_create_ssh_key(fluidstack_client):
    response = fluidstack_client.ssh_keys.create(
        name="test-ssh-key",
        public_key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINxBcojVFY/IWdyVjB7ZRXH0syGrUXx3ycweb7I67wqq test@local",
    )

    assert response.name == "test-ssh-key"
    assert (
        response.public_key
        == "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINxBcojVFY/IWdyVjB7ZRXH0syGrUXx3ycweb7I67wqq test@local"
    )
    assert response.id is not None


def test_list_ssh_key(fluidstack_client):
    ssh_key_list = fluidstack_client.ssh_keys.list()
    assert ssh_key_list is not None
    assert len(ssh_key_list) > 0


def test_delete_ssh_key(fluidstack_client):
    ssh_key_list = fluidstack_client.ssh_keys.list()
    assert ssh_key_list is not None
    assert len(ssh_key_list) > 0

    ssh_key_id = ssh_key_list[0].id
    response = fluidstack_client.ssh_keys.delete(ssh_key_id)
    assert response is None
