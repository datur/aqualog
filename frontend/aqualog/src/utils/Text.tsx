

export function toTitleCase(str: string | undefined): string {
    if (str === undefined){
        return ""
    }
    return str.toLowerCase().split(' ').map(function (word) {
      return (word.charAt(0).toUpperCase() + word.slice(1));
    }).join(' ');
  }