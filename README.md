Rsync-Snap
==========

*A python script that manages backup configuration profiles, input arguments, logging, ssh-connections, rsync with `--dest-link`, and linking logic to make a TimeMachine-ish incremental snapshot backup of a directory to another... even if it's on a remote host with SSH access*.


To-Do
-----

### v0.1

- [ ] Apply the massive comments of the previous attempt to bootstrap this idea in this script's bash precursor script to make understanding the project easier.
- [x] TDD - do it from the beginning, these are user and system files that are being handled.
- [ ] Basic argument parsing using `argparse` to simply parse the backup proflie name to use.
- [ ] Check that the backup profile name given is valid.
- [ ] Check that the standard `rsync-snap.yml` has a file in it:
    - For now just keep it in the same directory as the repo
    - Finally learning to use the standard `unittest` module.
- [ ] YAML config parsing.
    - [ ] `backup-name` **v0.1**
    - [ ] `source-dir` **v0.1**
    - [ ] `log-dir` **v0.2**
    - [ ] `dest-address` **v0.3**
    - [ ] `dest-port` **v0.3**
    - [ ] `dest-id` **v0.3**
    - [ ] `dest-ssh-name` **v0.3**
    - [ ] `dest-dir` **v0.3**
    - [ ] `systemd-log-level` **v0.4**
    - [ ] `post-backup-command` **v0.5**
- [ ] Validate that source path is correct and readable
- [ ] Check if destination has an initial backup.
- [ ] If not initial backup exists, format the command string to initialize the backup.
- [ ] After transfer is complete, rename the folder to a timestamp instead.
- [ ] After renaming the initial backup, create a symlink in the same directory that links to the latest backup, and name that link `latest`.
- [ ] Check for initial backup, and if it exists, format the correct command string to create the linked backup.
- [ ] Once executed completely, rename the folder to the current timestamp.
- [ ] Force relink `latest` to the newly backed up snapshot with its new timestamp named directory.
    - `ln -sf DEST_DIR/2018-02-26_T235901`

### v0.2

- [ ] When a transfer is in progress, the destination folder should be named `/in-progress-snapshot`.
- [ ] On restarting this script, it should first check if the above folder is visible.
- [ ] If it is, the symlink `latest` should be the `--link-dest` and `in-progress-snapshot/` shold be the destination directory.
- [ ] Now do the same old thing, where the in progress folder gets renamed by the same timestamp.
- [ ] Then again, relink `latest` to the new *latest* snapshot directory.
- [ ] Pipe verbose output `-P` into a log file specified by user, **IF** the config file wants it.

### v0.3

- [ ] Format proper ssh commands within the script.
- [ ] Parse ssh relevant parameters:
    - [ ] if a ssh config name is specified, use the ssh config file with the name given.
    - [ ] else look for specified connection details like address, port, id file.
    - [ ] otherwise throw error, that the config is ambigious and with incomplete connection info.
- [ ] Be able to detect if a previous snapshot has been made, if not perform the initial snapshot func
- [ ] Same as before, name the destination directory `in-progress-snapshot/` during the transfer.
- [ ] Make sure that all configurations can successfully form the right `rsync` & `ssh` commands.
- [ ] Be able to forward any ssh errors to STDOUT.
- [ ] On successful backup, as before, rename `in-progress-snapshot` to a timestamp
- [ ] Then `ln -sf DESTINATION_DIR/YYYY-MM-DD_THHmmSS ./latest`

### v0.4

- [ ] Properly validate user entered config options before running them and supply warning.
- [ ] Whether local or remote destinations are in use, allow for execution of scripts upon completion.
- [ ] If no config file is detected, give user instructions to create one, or an interactive prompt to have one generated for them.

### v0.5

- [ ] Create checksums in logs
- [ ] Trim logs to my manifest file format (basically CSV)
- [ ] Properly pipe logs of different levels to `systemd` on user config.
- [ ] Run quietly while still capturing logs.
- [ ] Be able to read output from rsync progress to come up with better transfer estimates.
    - [ ] You can run a `du -sh SOURCE_DIR` to get the total transfer time.
    - [ ] This might not be terribly easy or worth it since only deltas will be transferred.
    - [ ] Other suggestion is to parse the passed STDOUT to read rsync's progress programatically.
