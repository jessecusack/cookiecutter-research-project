
currentFolder = strrep(fullfile(pwd()), '\', '/');
project_path = strcat(currentFolder, '/../');  % Notez l'ajout de "/../" pour remonter d'un niveau
cd(project_path);

[~, project_name, ~] = fileparts(pwd);
project_folder = strrep(pwd(), '\', '/');

proj = matlab.project.createProject(strrep(fullfile(project_folder), '\', '/'));
addFolderIncludingChildFiles(proj,strrep(fullfile(project_folder, "/scripts"), '\', '/'));

proj.Name = project_name;
addStartupFile(proj, "scripts/src/matlab/startup.m");
addShutdownFile(proj, "scripts/src/matlab/shutdown.m");

files = dir; 
dirFlags = [files.isdir];
directories = files(dirFlags);
directories(contains({directories.name}, 'resources')) = [];

for k = 3:length(directories)
    currentDirectory = directories(k).name; 
    addFolderIncludingChildFiles(proj,strrep(fullfile(project_folder, currentDirectory), '\', '/'));
end